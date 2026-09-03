from client import AgentOpenTelemetrySpanTraceProfilerClient

def main():
    client = AgentOpenTelemetrySpanTraceProfilerClient()
    res = client.profile_agent_trace('trc_01')
    print('OpenTelemetry Span Profiler: ' + res['profile_id'] + ' (Trace: ' + res['root_trace_id'] + ')')
    print('Latency: ' + str(res['cumulative_latency_ms']) + 'ms | Tokens: ' + str(res['total_tokens_consumed']))
    print('Bottleneck: ' + res['bottleneck_span'])
    print('Trace Waterfall URL: ' + res['trace_waterfall_url'])

if __name__ == '__main__':
    main()
