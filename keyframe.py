class Keyframe:
    focal_length =  910
    # distortion
    p_point = 0
    def __init__(self, pose, features):
        self.pose = pose
        self.features = features
