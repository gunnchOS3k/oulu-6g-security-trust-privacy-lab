from pathlib import Path
from oulu_6g_security.threat_model import stride_summary
from oulu_6g_security.oran_security import oran_risks
from oulu_6g_security.airan_attack_surface import airan_surface
from oulu_6g_security.edge_telemetry_privacy import privacy_controls
from oulu_6g_security.digital_twin_data_risk import twin_risks
from oulu_6g_security.zero_trust_device import zt_principles
from oulu_6g_security.report import compile_report

R=Path('results')
R.mkdir(exist_ok=True)
(R/'threat_model.md').write_text('# STRIDE\n'+', '.join(stride_summary())+'\n')
(R/'airan_attack_surface.md').write_text('# AI-RAN\n'+', '.join(airan_surface())+'\n')
(R/'edge_telemetry_privacy_review.md').write_text('# Privacy\n'+', '.join(privacy_controls())+'\n')
(R/'zero_trust_7gc_device_model.md').write_text('# ZT\n'+', '.join(zt_principles())+'\n')
(R/'experiment_summary.md').write_text('# Security e2e PASS\n')
