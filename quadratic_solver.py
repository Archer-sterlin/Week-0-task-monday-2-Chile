from logging import exception


def quadraticSolver(a:int,b:int,c:int):
    try:
        step_one = ((b**2 - 4 * a * c)**0.5)
        answer_minus_b = (-b - step_one) / (2 * a)
        answer_plus_b = (-b + step_one) / (2 * a)
        return {"x_minus":answer_minus_b,
                "x_plus":answer_plus_b
                }
    except:
        return "How I want take divid by zero now?"



x = quadraticSolver(0,1,-9) 


    
        
