	?????]?@?????]?@!?????]?@	<??s2?Y?<??s2?Y?!<??s2?Y?"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$?????]?@??\5ϵ?Ah?>?]?@Y?Mc{-???*	D?l' ?%A2g
0Iterator::Model::Prefetch::FlatMap[0]::Generator_ѭWF?@!?By???X@)_ѭWF?@1?By???X@:Preprocessing2F
Iterator::Model4???????!???JRu?)?Eж???1_2??h?:Preprocessing2P
Iterator::Model::Prefetch????fd??!????eb?)????fd??1????eb?:Preprocessing2Y
"Iterator::Model::Prefetch::FlatMap&r?\F?@!?LԶ??X@)?ɋL??a?18?'l?3?:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 0.0% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	??\5ϵ???\5ϵ?!??\5ϵ?      ??!       "      ??!       *      ??!       2	h?>?]?@h?>?]?@!h?>?]?@:      ??!       B      ??!       J	?Mc{-????Mc{-???!?Mc{-???R      ??!       Z	?Mc{-????Mc{-???!?Mc{-???JCPU_ONLY