from wtforms import SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput

class MUltipleCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()