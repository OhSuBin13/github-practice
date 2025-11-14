from typing import Union, Optional

def add(x: Union[int, float], y: Union[int, float]) -> Optional[Union[int, float]]:
    try:
        result = x + y
    except Exception as e:
        print(e)
        return None
    
    return result

if __name__ == "__main__":
    print(add(5, 3))        # Output: 8
    print(add(2.5, 4.5))    # Output: 7.0
    print(add(1, 2.5))      # Output: 3.5