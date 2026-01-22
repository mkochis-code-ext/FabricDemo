# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "environment": {
# META       "environmentId": "153be2a3-3b94-8ed9-4809-73e0863d51a9",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# CELL ********************


# test Comment
import sempy_labs as labs
import sempy.fabric as fabric
from sempy_labs.tom import connect_semantic_model

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

workspace = fabric.get_workspace_id()
semantic_model_name = "demo_semantic_model"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


with connect_semantic_model(dataset=semantic_model_name, workspace=workspace, readonly=False) as tom:
    table_name = "sales"
    measure_name = "my_new_measure"
    expression = 'SUM(sales[Fake_Measure_1])'
    format_string = "#,##0"

    tom.add_measure(
         table_name = table_name
        ,measure_name = measure_name
        ,expression = expression
        ,format_string = format_string
    )


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
