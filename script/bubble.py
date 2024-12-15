import pandas as pd
import matplotlib.pyplot as plt


def test():
    import plotly.graph_objects as go

    # Sample data

    middle_labels = ['Requirements Variability', 'Architecture Variability', 'Implementation Variability',
                     'Verification and Validation', 'Variability Management', 'Orthogonal Variability']

    left_side_labels = ['Metric', 'Tool', 'Model', 'Method', 'Process']
    right_side_labels = ['Evaluation Research', 'Validation Research', 'Solution Proposal', 'Philosophical Paper',
                         'Experience Report', 'Opinion Paper']
    # left_counts = [4, 10, 42, 46, 16]
    # right_counts = [50, 0, 56, 14, 8, 0]

    x_labels = left_side_labels + [""] + right_side_labels

    data_left = {
        'Requirements Variability': {
            'Metric': 3,
            'Tool': 6,
            'Model': 15,
            'Method': 17,
            'Process': 4
        },
        'Architecture Variability': {
            'Metric': 0,
            'Tool': 1,
            'Model': 11,
            'Method': 15,
            'Process': 8
        },
        'Implementation Variability': {
            'Metric': 0,
            'Tool': 0,
            'Model': 8,
            'Method': 4,
            'Process': 1
        },
        'Verification and Validation': {
            'Metric': 0,
            'Tool': 1,
            'Model': 11,
            'Method': 15,
            'Process': 8
        },
        'Variability Management': {
            'Metric': 0,
            'Tool': 1,
            'Model': 11,
            'Method': 15,
            'Process': 8
        },
        'Orthogonal Variability': {
            'Metric': 0,
            'Tool': 1,
            'Model': 11,
            'Method': 15,
            'Process': 8
        },
    }

    data_right = {
        'Requirements Variability': {
            'Evaluation Research': 13,
            'Validation Research': 0,
            'Solution Proposal': 21,
            'Philosophical Paper': 2,
            'Experience Report': 0,
            'Opinion Paper': 0
        },
        'Architecture Variability': {
            'Evaluation Research': 17,
            'Validation Research': 0,
            'Solution Proposal': 19,
            'Philosophical Paper': 5,
            'Experience Report': 3,
            'Opinion Paper': 0
        },
        'Implementation Variability': {
            'Evaluation Research': 9,
            'Validation Research': 0,
            'Solution Proposal': 3,
            'Philosophical Paper': 4,
            'Experience Report': 1,
            'Opinion Paper': 0
        },
        'Verification and Validation': {
            'Evaluation Research': 6,
            'Validation Research': 0,
            'Solution Proposal': 4,
            'Philosophical Paper': 0,
            'Experience Report': 0,
            'Opinion Paper': 0
        },
        'Variability Management': {
            'Evaluation Research': 3,
            'Validation Research': 0,
            'Solution Proposal': 7,
            'Philosophical Paper': 2,
            'Experience Report': 4,
            'Opinion Paper': 0
        },
        'Orthogonal Variability': {
            'Evaluation Research': 2,
            'Validation Research': 0,
            'Solution Proposal': 2,
            'Philosophical Paper': 1,
            'Experience Report': 0,
            'Opinion Paper': 0
        }
    }

    # Create figure_1
    fig = go.Figure()

    left_count_y = 0
    for topic in data_left:
        count_x = 0
        left_count_y += 1
        for item, count in data_left[topic].items():
            count_x -= 1
            if count > 0:
                if count < 5:
                    fig.add_trace(go.Scatter(
                        x=[count_x],  # Position all left-side bubbles at x = -1
                        y=[left_count_y],
                        mode='markers+text',
                        marker=dict(size=[count * 3], sizemode='diameter'),
                        text=[count],
                        textposition='bottom center',
                        hoverinfo='text',
                        name='Contribution Facet'
                    ))
                else:
                    fig.add_trace(go.Scatter(
                        x=[count_x],  # Position all left-side bubbles at x = -1
                        y=[left_count_y],
                        mode='markers+text',
                        marker=dict(size=[count * 3], sizemode='diameter'),
                        text=[count],
                        textposition='bottom center',
                        hoverinfo='text',
                        name='Contribution Facet'
                    ))

    right_count_y = 0
    for topic in data_right:
        count_x = 0
        right_count_y += 1
        for item, count in data_right[topic].items():
            count_x += 1
            if count > 0:
                if count < 5:
                    fig.add_trace(go.Scatter(
                        x=[count_x],  # Position all left-side bubbles at x = -1
                        y=[right_count_y],
                        mode='markers+text',
                        marker=dict(size=[count * 5], sizemode='diameter'),
                        text=[count],
                        textposition='middle center',
                        hoverinfo='text',
                        name='Contribution Facet'
                    ))
                else:
                    fig.add_trace(go.Scatter(
                        x=[count_x],  # Position all left-side bubbles at x = -1
                        y=[right_count_y],
                        mode='markers+text',
                        marker=dict(size=[count * 3], sizemode='diameter'),
                        text=[count],
                        textposition='middle center',
                        hoverinfo='text',
                        name='Contribution Facet'
                    ))

    fig.update_layout(
        title='Bubble Chart for Systematic Mapping Study',
        xaxis=dict(title='', tickvals=list(range(0 - len(left_side_labels), len(right_side_labels) + 1)),
                   ticktext=x_labels),
        yaxis=dict(title='', tickvals=list(range(1, len(middle_labels) + 1)),
                   ticktext=middle_labels, showgrid=True, shift=5),
        showlegend=False,
        height=800,
        width=1200,
        margin=dict(l=100, r=100)
    )

    # Show the figure_1
    fig.show()


def topic_vs_research_type():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")

    grouped_data = df.groupby(["research type - final", "topic"]).size().reset_index(name="count")

    print(grouped_data["research type - final"])
    grouped_data["research type - final"] = grouped_data["research type - final"].replace({
        "Solution proposal, Evaluation research": "Solution proposal+\nEvaluation research",
        "Solution proposal, Validation research": "Solution proposal+\nValidation research",
    }
    )

    # Extract unique research types and topics
    research_types = grouped_data["research type - final"].unique()
    topics = grouped_data["topic"].unique()

    plt.figure(figsize=(10, 8))

    for _, row in grouped_data.iterrows():
        research_type = row['research type - final']
        topic = row['topic']
        count = row['count']

        x_pos = research_types.tolist().index(research_type)
        y_pos = topics.tolist().index(topic)

        plt.scatter(
            x=x_pos,
            y=y_pos,
            s=count * 300,
            alpha=0.5,
        )

        plt.text(
            x_pos,
            y_pos - 0.05,
            str(count),
            ha='center',
            va='bottom',
            fontsize=12,
        )

    plt.xticks(range(len(research_types)), research_types, rotation=45, ha='right', fontsize=12)
    plt.yticks(range(len(topics)), topics, fontsize=12)
    plt.grid(alpha=0.5)

    # plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.15)
    plt.tight_layout()
    plt.show()

topic_vs_research_type()