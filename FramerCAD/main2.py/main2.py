import tkinter as tk
from tkinter import ttk
from math import sqrt

class HouseDraftingTool:
    def __init__(self, root):
        self.root = root
        self.root.title("House Drafting Tool")
        
        # Constants
        self.WIDTH, self.HEIGHT = 1000, 700
        self.GRID_SIZE = 20
        self.COLORS = {
            'WHITE': '#FFFFFF',
            'BLACK': '#000000',
            'RED': '#FF0000',
            'BLUE': '#0000FF',
            'GRAY': '#C8C8C8'
        }
        
        # Drawing variables
        self.drawing = False
        self.current_wall = []
        self.walls = []  # Each wall is ([points], width)
        self.current_wall_width = 10
        self.snap_to_grid = True
        
        # Create UI
        self.create_widgets()
        
        # Bind events
        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.root.bind("<Escape>", self.on_escape)
        self.root.bind("<Control-z>", self.on_undo)
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=self.WIDTH, height=self.HEIGHT, 
                               bg=self.COLORS['WHITE'], cursor="cross")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Control panel
        control_frame = ttk.Frame(main_frame, width=200)
        control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        
        # Wall width control
        ttk.Label(control_frame, text="Wall Width:").pack(pady=(10, 0))
        self.width_label = ttk.Label(control_frame, text=f"{self.current_wall_width}px")
        self.width_label.pack()
        
        width_controls = ttk.Frame(control_frame)
        width_controls.pack(pady=5)
        
        ttk.Button(width_controls, text="-", width=3, 
                  command=lambda: self.adjust_wall_width(-5)).pack(side=tk.LEFT, padx=2)
        ttk.Button(width_controls, text="+", width=3, 
                  command=lambda: self.adjust_wall_width(5)).pack(side=tk.LEFT, padx=2)
        
        # Snap to grid toggle
        self.snap_button = ttk.Button(control_frame, text="Snap: ON", 
                                     command=self.toggle_snap)
        self.snap_button.pack(pady=10)
        
        # Clear button
        ttk.Button(control_frame, text="Clear All", command=self.clear_all).pack(pady=5)
        
        # Draw the grid
        self.draw_grid()
    
    def draw_grid(self):
        for x in range(0, self.WIDTH, self.GRID_SIZE):
            self.canvas.create_line(x, 0, x, self.HEIGHT, fill=self.COLORS['GRAY'], tags="grid")
        for y in range(0, self.HEIGHT, self.GRID_SIZE):
            self.canvas.create_line(0, y, self.WIDTH, y, fill=self.COLORS['GRAY'], tags="grid")
    
    def draw_walls(self):
        # Clear existing walls (except grid)
        self.canvas.delete("wall")
        self.canvas.delete("wall_center")
        
        for wall in self.walls:
            points, width = wall
            if len(points) >= 2:
                for i in range(len(points) - 1):
                    x1, y1 = points[i]
                    x2, y2 = points[i+1]
                    
                    # Calculate perpendicular vector for wall thickness
                    dx = x2 - x1
                    dy = y2 - y1
                    length = max(1, sqrt(dx*dx + dy*dy))
                    nx = -dy/length
                    ny = dx/length
                    
                    # Create polygon points for the wall
                    polygon_points = [
                        x1 + nx*width/2, y1 + ny*width/2,
                        x1 - nx*width/2, y1 - ny*width/2,
                        x2 - nx*width/2, y2 - ny*width/2,
                        x2 + nx*width/2, y2 + ny*width/2
                    ]
                    
                    # Draw the wall
                    self.canvas.create_polygon(
                        polygon_points, 
                        fill=self.COLORS['BLUE'], 
                        outline=self.COLORS['BLACK'],
                        tags="wall"
                    )
                    
                    # Draw the center line
                    self.canvas.create_line(
                        x1, y1, x2, y2, 
                        fill=self.COLORS['BLACK'], 
                        width=2,
                        tags="wall_center"
                    )
    
    def snap_point(self, point):
        if self.snap_to_grid:
            x, y = point
            return (round(x / self.GRID_SIZE) * self.GRID_SIZE, 
                    round(y / self.GRID_SIZE) * self.GRID_SIZE)
        return point
    
    def on_left_click(self, event):
        # Check if clicking on UI elements (not implemented in this version)
        # Start drawing a wall
        self.drawing = True
        snapped_pos = self.snap_point((event.x, event.y))
        self.current_wall = [snapped_pos]
        
        # Draw the first point
        self.canvas.delete("current_point")
        self.canvas.create_oval(
            snapped_pos[0]-5, snapped_pos[1]-5,
            snapped_pos[0]+5, snapped_pos[1]+5,
            fill=self.COLORS['RED'],
            tags="current_point"
        )
    
    def on_right_click(self, event):
        if self.drawing and len(self.current_wall) > 1:
            # Finish the current wall
            self.walls.append((self.current_wall.copy(), self.current_wall_width))
            self.current_wall = []
            self.drawing = False
            self.draw_walls()
            self.canvas.delete("current_walline")
            self.canvas.delete("current_point")
    
    def on_mouse_move(self, event):
        if self.drawing:
            snapped_pos = self.snap_point((event.x, event.y))
            
            if len(self.current_wall) > 0 and snapped_pos != self.current_wall[-1]:
                if len(self.current_wall) == 1:
                    self.current_wall.append(snapped_pos)
                else:
                    self.current_wall[-1] = snapped_pos
                
                # Draw preview of current wall
                self.canvas.delete("current_walline")
                
                if len(self.current_wall) >= 2:
                    # Draw the wall preview
                    x1, y1 = self.current_wall[0]
                    x2, y2 = self.current_wall[-1]
                    
                    # Calculate perpendicular vector for wall thickness
                    dx = x2 - x1
                    dy = y2 - y1
                    length = max(1, sqrt(dx*dx + dy*dy))
                    nx = -dy/length
                    ny = dx/length
                    
                    # Create polygon points for the wall preview
                    polygon_points = [
                        x1 + nx*self.current_wall_width/2, y1 + ny*self.current_wall_width/2,
                        x1 - nx*self.current_wall_width/2, y1 - ny*self.current_wall_width/2,
                        x2 - nx*self.current_wall_width/2, y2 - ny*self.current_wall_width/2,
                        x2 + nx*self.current_wall_width/2, y2 + ny*self.current_wall_width/2
                    ]
                    
                    self.canvas.create_polygon(
                        polygon_points, 
                        fill=self.COLORS['BLUE'], 
                        outline=self.COLORS['BLACK'],
                        tags="current_walline"
                    )
                    
                    # Draw the center line preview
                    self.canvas.create_line(
                        x1, y1, x2, y2, 
                        fill=self.COLORS['BLACK'], 
                        width=2,
                        tags="current_walline"
                    )
    
    def on_escape(self, event):
        if self.drawing:
            self.current_wall = []
            self.drawing = False
            self.canvas.delete("current_walline")
            self.canvas.delete("current_point")
    
    def on_undo(self, event):
        if self.walls:
            self.walls.pop()
            self.draw_walls()
    
    def adjust_wall_width(self, delta):
        self.current_wall_width = max(5, self.current_wall_width + delta)
        self.width_label.config(text=f"{self.current_wall_width}px")
    
    def toggle_snap(self):
        self.snap_to_grid = not self.snap_to_grid
        self.snap_button.config(text="Snap: ON" if self.snap_to_grid else "Snap: OFF")
    
    def clear_all(self):
        self.walls = []
        self.current_wall = []
        self.drawing = False
        self.canvas.delete("wall")
        self.canvas.delete("wall_center")
        self.canvas.delete("current_walline")
        self.canvas.delete("current_point")

if __name__ == "__main__":
    root = tk.Tk()
    app = HouseDraftingTool(root)
    root.mainloop()