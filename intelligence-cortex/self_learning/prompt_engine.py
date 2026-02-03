class SelfLearningPrompter:
    @staticmethod
    def generate_post_mortem_prompt(trade_log, context):
        return f"Analyze trade: {trade_log} vs Context: {context}"
