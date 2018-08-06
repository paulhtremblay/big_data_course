http://localhost:4040/jobs/

=> 

click on stages 

click on first active
--conf spark.ui.showConsoleProgress=true

What you get is a Console Progress Bar, [Stage 7: shows the stage you are in now, and (14174 + 5) / 62500] is (numCompletedTasks + numActiveTasks) / totalNumOfTasksInThisStage]. The progress bar shows numCompletedTasks / totalNumOfTasksInThisStage.
