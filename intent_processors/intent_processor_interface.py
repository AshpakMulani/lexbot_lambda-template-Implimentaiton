from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class IntentProcessorInterface(ABC):
    """
    A class to provide base interface for other classes whihc implements
    intent processor using 'process' method.
    
    Attributes
    ----------
        None 
        
    Methods
    -------
        process():
            abstract method for child classes to implement.
        
    """
    
    @abstractmethod
    def process(self) -> Optional[Dict[str, Any]]:
        pass
    