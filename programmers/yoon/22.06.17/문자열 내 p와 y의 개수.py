def solution(s):
    if s.lower().count('p') == s.lower().count('y'):
        return True
    else:
        return False
    
    """
    # 더 간단하게
    return s.lower().count('p') == s.lower().count('y')
    """