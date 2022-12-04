CREATE TABLE IF NOT EXISTS user_input (
	country varchar(100),
	fund varchar(100),
	portfolio varchar(100),
	company_performance int,
	company_performance_comment TEXT,
	company_stronger int,
	company_stronger_comment TEXT,
	gap_status int,
	gap_status_comment TEXT,
	relative_peer int,
	relative_peer_comment TEXT,
	time_stamp TIMESTAMP

)