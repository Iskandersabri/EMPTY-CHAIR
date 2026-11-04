## Data Cleaning & Scope Decisions

### Rows removed:
1. **Children (Age < 18)**: removed
   - Rationale: minors do not decide attendance; parents do. 
     Including them mixes two different behavioral processes.
2. **Negative ages**: removed (impossible values)
3. **Negative WaitingDay**: removed (AppointmentDay before ScheduledDay = impossible)
4. **Ages > 90**: removed (rare, insufficient data to learn from)

### Result:
- Original: 110,527
- Remaining: 79,575 (72%)
- Total removed: 30,952 (28%)

### Accepted trade-off:
- Model applies only to adults (18-90)
- Cannot predict pediatric no-shows
