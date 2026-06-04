from oulu_6g_security.threat_model import stride_summary

def test_stride():
    assert len(stride_summary())==6
