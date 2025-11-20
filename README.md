# Connect 4 AI  
## Minimax Search with Alpha–Beta Pruning

**Authors**  
- Taeyoon Kim
- Allen Solomon
- Arthur Lee
- Hengyi Liu  

This project implements an intelligent **Connect 4 AI** using the **Minimax algorithm** enhanced with **Alpha–Beta pruning**. Its purpose is to demonstrate adversarial search in a zero-sum environment and highlight the performance improvements gained through pruning and move ordering.

### Features
- Complete Connect 4 game on a 6×7 board  
- Minimax search with configurable depth  
- Alpha–Beta pruning for major speedups  
- Center-out move ordering for stronger pruning efficiency  
- Custom heuristic evaluation:  
  - counts unblocked 1-, 2-, and 3-in-a-row patterns  
  - rewards center-column control  
- Deterministic, challenging AI behavior at higher depths  
- CLI-based gameplay

### Project Structure
```
.
├── README.md                           # Documentation (this file)
├── minimax_connect4(no_alpha_beta).py  # Implementation without Alpha-Beta pruning for comparison
├── minimax_connect4.py                 # Main implementation
```

### How to Run

**Requirements**  
- Python 3

**Start the Game**  
```bash
python3 connect4.py
```

You will see:  
```
Connect Four - human (O) vs AI (X). Columns 0..6
```
Enter a column number (0–6) on your turn.

The AI plays as **X**, and the human plays as **O**.

Enjoy playing against our AI!

** You can click the COMP560_Final_Project.pdf to view our paper. Make sure to download to view it as preview is not working.
