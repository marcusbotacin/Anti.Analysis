rule CPU_Detector : CPU
{
	meta:
	description = "CPU Instruction Detector"

	strings:
		$str={0F 00}
		$sidt={0F 01}

	condition:
		$str or $sidt
}
