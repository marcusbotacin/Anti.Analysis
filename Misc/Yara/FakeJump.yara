rule FakeJump_Detector : FakeJump
{
	meta:
	description = "FakeJump Detector"

	strings:
		$seq={31 ?? 0F}

	condition:
		$seq
}
