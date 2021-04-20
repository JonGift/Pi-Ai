## Optimized Model Stats
> **Precision**
> - True Positives / All detections   

> **Recall**
> - True Positives / All ground truth detections

## Optimized Model Detection Results
using multi_channel_face_detection_demo (from open_model_zoo)
**using .bin & .xml**
- **Confidence Threshold**: 50%
- **Total Images**: 42
- **Ground Truth Detections**: 82
- **All Detections**: 38
- **True Positives**: 34
- **False Postitives**: 4
- **False Negatives**: 48

> - **Precision**: .894 (89%)
> - **Recall**: .414 (41%)

## Full Model Detection Results
using object detection tutorial (from TensorFlow models/research/object_detection)
**using frozen_inference_graph.pb and .pbtxt**
- **Confidence Threshold**: 50%
- **Total Images**: 40
- **Ground Truth Detections**: 101
- **All Detections**: 69
- **True Positives**: 66
- **False Postitives**: 1
- **False Negatives**: 32

> - **Precision**: .956 (96%)
> - **Recall**: .653 (65%)
