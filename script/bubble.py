import pandas as pd
import matplotlib.pyplot as plt


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


def objective_vs_target():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")
    df = df.assign(
        **{
            "test objective": df["test objective"].str.split(", "),
            "test target": df["test target"].str.split(", "),
        }
    ).explode("test objective").explode("test target")

    grouped_data = df.groupby(["test objective", "test target"]).size().reset_index(name="count")
    objectives = grouped_data["test objective"].unique()
    targets = grouped_data["test target"].unique()
    plt.figure(figsize=(10, 5.5))

    for _, row in grouped_data.iterrows():
        objective = row['test objective']
        target = row['test target']
        count = row['count']
        x_pos = list(targets).index(target)
        y_pos = list(objectives).index(objective)

        plt.scatter(
            x=x_pos,
            y=y_pos,
            s=count * 300,
            alpha=0.5,
        )

        plt.text(
            x_pos,
            y_pos - 0.1,
            str(count),
            ha='center',
            va='bottom',
            fontsize=14,
        )

    plt.xlabel("test objective", fontsize=16)
    plt.ylabel('test target', fontsize=16)
    plt.xticks(range(len(targets)), targets, rotation=45, ha='right', fontsize=14)
    plt.yticks(range(len(objectives)), objectives, fontsize=14)
    plt.grid(alpha=0.5)
    plt.ylim(-0.5, 5.5)

    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/ruizhengu/Projects/XR-testing-study/figure/objective_vs_target.png', dpi=300)


def eval_env_vs_metric():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")

    df = df.assign(
        **{
            "eval metrics": df["eval metrics"].str.split(", "),
            "eval environment": df["eval environment"].str.split(", "),
        }
    ).explode("eval metrics").explode("eval environment")

    grouped_data = df.groupby(["eval metrics", "eval environment"]).size().reset_index(name="count")
    grouped_data["eval metrics"] = grouped_data["eval metrics"].replace({
        "standard ML performance metrics": "standard ML metrics",
    }
    )

    objectives = grouped_data["eval metrics"].unique()
    targets = grouped_data["eval environment"].unique()
    plt.figure(figsize=(10, 6))

    for _, row in grouped_data.iterrows():
        objective = row['eval metrics']
        target = row['eval environment']
        count = row['count']
        y_pos = list(targets).index(target)
        x_pos = list(objectives).index(objective)

        plt.scatter(
            x=x_pos,
            y=y_pos,
            s=count * 300,
            alpha=0.5,
        )

        plt.text(
            x_pos,
            y_pos - 0.1,
            str(count),
            ha='center',
            va='bottom',
            fontsize=14,
        )

    plt.xlabel("evaluation metric", fontsize=16)
    plt.ylabel('evaluation environment', fontsize=16)
    plt.yticks(range(len(targets)), targets, fontsize=14)
    plt.xticks(range(len(objectives)), objectives, fontsize=14, rotation=45, ha='right')
    plt.grid(alpha=0.5)
    plt.ylim(-0.5, 5.5)

    plt.tight_layout()
    plt.show()

# topic_vs_research_type()
# objective_vs_target()
eval_env_vs_metric()