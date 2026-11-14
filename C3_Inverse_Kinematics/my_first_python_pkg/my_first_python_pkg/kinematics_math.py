import math

def inverse_kinematics(x: float, y:float, L1: float = 14.0, L2: float = 15.5):
    if x < 0.0 or y < 0.0:
        raise ValueError("Target coordinate must be non-negative...")

    r_square = x*x + y*y
    r = math.sqrt(r_square)

    min_reach = abs(L1-L2)
    max_reach = L1 + L2

    if r< min_reach or r > max_reach:
        raise ValueError(f"outside reachable area...")
    
    cos_t2 = (r_square - L1**2 - L2**2)/ (2*L1 * L2)
    cos_t2 = max(-1.0, min(1.0, cos_t2))
    t2 = math.acos(cos_t2)


    phi = math.atan2(y,x)
    alpha = math.atan2(L2 * math.sin(t2), L1+ L2*math.cos(t2))
    theta1 = phi+alpha

    servo1 = 180.0 - math.degrees(theta1)
    servo2 = math.degrees(t2)

    if not(0.0<= servo1 <= 180.0):
        raise ValueError('joint 1 angle exceeds servo limits')
        
    if not(0.0 <= servo2 <= 180.0):
        raise ValueError('joint 2 angle exceeds servo limits')
    
    return servo1, servo2


def forward_kinematics(servo1: float, servo2: float, L1 : float = 14.0, L2 : float = 15.5):
    if not(0.0<= servo1 <= 180.0):
        raise ValueError('joint 1 angle exceeds servo limits')
        
    if not(0.0 <= servo2 <= 180.0):
        raise ValueError('joint 2 angle exceeds servo limits')
    
    theta1 = math.radians(180.0 - servo1)
    t2 = math.radians(servo2)

    theta2_global = theta1 - t2

    x = L1* math.cos(theta1) + L2 * math.cos(theta2_global)
    y = L1* math.sin(theta1) + L2 * math.sin(theta2_global)

    return x , y