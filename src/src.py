import tkinter as tk
import time
root = tk.Tk()
root.title("Workout Program")
label = tk.Label(root, text="This is a workout program")
label.pack()
root.mainloop()
 
class Exercise:
    def __init__(self, name="None", sets=0, reps=0, muscle_group1="None", muscle_group2="None", summary='') -> None:
        self.name = name
        self.sets = sets
        self.reps = reps
        self.muscle_group1 = muscle_group1
        self.muscle_group2 = muscle_group2
        self.summary = summary

    # Getters for each instance variable
    def get_name(self):
        return self.name

    def get_sets(self):
        return self.sets

    def get_reps(self):
        return self.reps

    def get_muscle_group1(self):
        return self.muscle_group1

    def get_muscle_group2(self):
        return self.muscle_group2

    def get_summary(self):
        return self.summary

    # Setters for each instance variable
    def set_name(self, name):
        self.name = name

    def set_sets(self, sets):
        self.sets = sets

    def set_reps(self, reps):
        self.reps = reps

    def set_muscle_group1(self, muscle_group1):
        self.muscle_group1 = muscle_group1

    def set_muscle_group2(self, muscle_group2):
        self.muscle_group2 = muscle_group2

    def set_summary(self, summary):
        self.summary = summary


# Example of exercises, maybe we want to add a way to make your own..?
bench_press = Exercise("Barbell Bench Press", 0, 0, "Chest", "Triceps, Front Deltoids", "Lie on a flat bench, grip the barbell, and press it from your chest to arms fully extended.")
inc_bench_press = Exercise("Incline Barbell Bench Press", 0, 0, "Chest", "Triceps, Front Deltoids", "Lie on an incline bench, grip the barbell, and press it from your chest to arms fully extended.")
chest_press = Exercise("Chest Press", 0, 0, "Chest", "Triceps, Front Deltoids", "Sit on a chest press machine and press the handles forward until arms are fully extended.")
dumbbell_fly = Exercise("Dumbbell Fly", 0, 0, "Chest", "Front Deltoids", "Lie on a flat bench with dumbbells in hand, lower arms out to sides, then bring them together above your chest.")
cable_fly = Exercise("Cable Fly", 0, 0, "Chest", "Front Deltoids", "Stand between cable machines, grab the handles, and pull them together in front of you while maintaining slightly bent arms.")
dips = Exercise("Dips", 0, 0, "Chest", "Triceps, Deltoids", "Grip parallel bars and lower your body until your arms are at 90 degrees, then push back up.")
tricep_pushdown = Exercise("Tricep Pushdown", 0, 0, "Triceps", "", "Using a cable machine, grip the bar and push it down until your arms are fully extended.")
skull_crusher = Exercise("Skull Crusher", 0, 0, "Triceps", "", "Lie on a bench with an EZ bar and lower it toward your forehead, then extend your arms to press the bar back up.")
squat = Exercise("Barbell Squat", 0, 0, "Quads", "Glutes, Hamstrings", "Stand with feet shoulder-width apart, barbell on upper back, and lower yourself into a squat before standing back up.")
deadlift = Exercise("Deadlift", 0, 0, "Back", "Hamstrings, Glutes", "Grip the barbell on the floor, hinge at the hips, and lift the bar while keeping your back straight.")
romanian_deadlift = Exercise("Romanian Deadlift", 0, 0, "Hamstrings", "Glutes", "With a barbell, lower it by hinging at the hips while keeping your legs straight, then return to standing.")
leg_press = Exercise("Leg Press", 0, 0, "Quads", "Glutes", "Sit on the leg press machine, place feet on the platform, and push it away by extending your legs.")
lunges = Exercise("Lunges", 0, 0, "Quads", "Glutes, Hamstrings", "Step forward with one leg, lower your hips until both knees are at 90-degree angles, and push back up.")
calf_raise = Exercise("Calf Raise", 0, 0, "Calves", "", "Stand on a raised surface, lift your heels off the ground by contracting your calves, then lower them back down.")
lat_pull_down = Exercise("Lat Pull Down", 0, 0, "Back", "Biceps", "Sit at a lat pull-down machine, grip the bar, and pull it down to your chest while keeping your back straight.")
pull_up = Exercise("Pull Up", 0, 0, "Back", "Biceps", "Grip a pull-up bar with palms facing away and pull your body up until your chin is over the bar.")
barbell_row = Exercise("Barbell Row", 0, 0, "Back", "Biceps", "Bend over with a barbell and row it to your lower chest, keeping your back straight.")
dumbbell_row = Exercise("Dumbbell Row", 0, 0, "Back", "Biceps", "Place one knee on a bench, grip a dumbbell with the other hand, and row it to your side while keeping your back straight.")
shoulder_press = Exercise("Shoulder Press", 0, 0, "Shoulders", "Triceps", "Grip a barbell or dumbbells at shoulder height and press them overhead until your arms are fully extended.")
lateral_raise = Exercise("Lateral Raise", 0, 0, "Shoulders", "", "Stand with dumbbells at your sides and lift them out to the sides until your arms are parallel to the floor.")
front_raise = Exercise("Front Raise", 0, 0, "Shoulders", "Front Deltoids", "Hold dumbbells in front of your thighs and raise them in front of you until your arms are parallel to the floor.")
face_pull = Exercise("Face Pull", 0, 0, "Shoulders", "Rear Deltoids", "Using a cable machine with a rope attachment, pull the rope toward your face, keeping your elbows high.")
bicep_curl = Exercise("Bicep Curl", 0, 0, "Biceps", "", "Stand with dumbbells or a barbell and curl the weights up to your shoulders while keeping your elbows stationary.")
hammer_curl = Exercise("Hammer Curl", 0, 0, "Biceps", "Forearms", "Hold dumbbells with palms facing each other and curl them toward your shoulders.")
preacher_curl = Exercise("Preacher Curl", 0, 0, "Biceps", "", "Sit at a preacher bench with an EZ bar and curl the bar toward your shoulders while keeping your upper arms on the pad.")
plank = Exercise("Plank", 0, 0, "Core", "", "Hold a position with your forearms and toes on the ground, keeping your body straight and core engaged.")
sit_up = Exercise("Sit-Up", 0, 0, "Core", "", "Lie on your back with knees bent, then sit up toward your knees and lower back down.")
russian_twist = Exercise("Russian Twist", 0, 0, "Core", "Obliques", "Sit on the floor, lean back slightly, and twist your torso side to side while holding a weight or medicine ball.")

