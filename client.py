class AgentOpenTelemetrySpanTraceProfilerClient:
    def profile_agent_trace(self, root_trace_id='trc_span_9918', spans=None):
        if spans is None:
            spans = [
                {'span_id': 'spn_1', 'name': 'Planner_Decompose', 'duration_ms': 142.5, 'tokens_in': 520, 'tokens_out': 180},
                {'span_id': 'spn_2', 'name': 'Tool_Database_Query', 'duration_ms': 48.2, 'status': 'OK'},
                {'span_id': 'spn_3', 'name': 'LLM_Synthesize_Answer', 'duration_ms': 310.0, 'tokens_in': 1200, 'tokens_out': 340}
            ]
        total_ms = sum([s.get('duration_ms', 0) for s in spans])
        total_tokens = sum([s.get('tokens_in', 0) + s.get('tokens_out', 0) for s in spans])
        return {
            'profile_id': 'prf_span_9918',
            'root_trace_id': root_trace_id,
            'total_spans_count': len(spans),
            'cumulative_latency_ms': round(total_ms, 2),
            'total_tokens_consumed': total_tokens,
            'bottleneck_span': 'LLM_Synthesize_Answer',
            'trace_waterfall_url': 'https://tracing.phoenix.genpark.ai/traces/9918.json'
        }
