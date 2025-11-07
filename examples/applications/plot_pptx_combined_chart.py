"""
=======================================================
Create a combined line and column chart in a PowerPoint
=======================================================

This example shows how to build a chart that mixes clustered
columns and a line series in the same chart area using the
``python-pptx`` package. The resulting presentation contains
one slide summarising quarterly financial results with both the
column series and the line series plotted against the primary
value axis.

To run the example you need to install ``python-pptx`` first::

    pip install python-pptx

"""

from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import (
    XL_AXIS_GROUP,
    XL_CHART_TYPE,
    XL_LEGEND_POSITION,
    XL_MARKER_STYLE,
)
from pptx.util import Inches, Pt


def build_presentation() -> Presentation:
    """Return a presentation with a combination chart example."""
    prs = Presentation()
    slide_layout = prs.slide_layouts[5]  # Title Only layout in the default template
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = "Quarterly performance overview"

    chart_data = CategoryChartData()
    chart_data.categories = ["Q1", "Q2", "Q3", "Q4"]
    chart_data.add_series("Revenue", (19.2, 21.4, 16.7, 23.8))
    chart_data.add_series("Expenses", (11.3, 12.6, 9.8, 13.1))
    chart_data.add_series("Gross margin", (41, 41, 41, 45))

    x, y, cx, cy = Inches(1), Inches(1.75), Inches(8), Inches(4.5)
    chart = slide.shapes.add_chart(
        XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data
    ).chart

    chart.has_legend = True
    chart.legend.position = XL_LEGEND_POSITION.BOTTOM
    chart.legend.include_in_layout = False

    primary_plot = chart.chart_groups[0]
    primary_plot.overlap = -10
    primary_plot.gap_width = 60

    for series in chart.series[:2]:
        fill = series.format.fill
        fill.solid()
        if series.name == "Revenue":
            fill.fore_color.rgb = RGBColor(91, 155, 213)
        else:
            fill.fore_color.rgb = RGBColor(237, 125, 49)
        series.data_labels.show_value = True

    # Convert the last series to a line plot while keeping it on the primary axis.
    plot = chart.plots[0]
    line_series = plot.series[-1]
    line_series.chart_type = XL_CHART_TYPE.LINE_MARKERS
    line_series.axis_group = XL_AXIS_GROUP.PRIMARY
    line_series.marker.style = XL_MARKER_STYLE.CIRCLE
    line_series.marker.size = 9
    line_series.format.line.width = Pt(2.25)
    line_series.format.line.color.rgb = RGBColor(165, 165, 165)
    line_series.data_labels.show_value = True

    chart.value_axis.has_major_gridlines = True
    chart.value_axis.axis_title.text_frame.text = "USD (millions)"
    chart.value_axis.minimum_scale = 0
    chart.value_axis.maximum_scale = 50

    chart.category_axis.axis_title.text_frame.text = "Quarter"

    return prs


def main(filename: str = "combined_line_column_chart.pptx") -> None:
    """Create and save the demonstration presentation."""
    presentation = build_presentation()
    presentation.save(filename)


if __name__ == "__main__":
    main()
