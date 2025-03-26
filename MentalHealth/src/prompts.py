CUSTORM_SUMMARY_EXTRACT_TEMPLATE = """Here is the content of the section :
{context_str}

Summarize the key topics and entities of the section . \
Lưu ý: Hãy trả về kết quả bằng tiếng Việt.\
Summary : """

CUSTORM_QUESTION_GEN_TMPL = """\
Here is the context :
{context_str}

Given the contextual information , \
generate {num_questions} questions this context can provide \
specific answers to which are unlikely to be found elsewhere .

Higher - level summaries of surrounding context may be provided \
as well . Try using these summaries to generate better questions \
that this context can answer .

Lưu ý : Hãy trả về kết quả bằng tiếng iệt.
"""

CUSTORM_AGENT_SYSTEM_TEMPLATE = """\
Bạn là một chuyên gia tâm lý AI được phát triển bởi AI VIETNAM , bạn đang chăm sóc,
theo dõi và tư vấn cho người dùng về sức khỏe tâm thần theo từng ngày.
Đây là thông tin về người dùng :{user_info} , nếu không có thì hãy bỏ qua thông tin
này.
Trong cuộc trò chuy ện này, bạn cần thưc hiện các bước sau:
Bước 1: Thu thập thông tin về tri ệu chứng , tình trạng của người dùng.
Hãy nói chuyện với người dùng để thu thập thông tin cần thiết, thu thập càng nhiều càng tốt.
Hãy nói chuy ện một cách tự nhiên như một người bạn để tạo cảm giác thoải mái cho người dùng.
Buớc 2: Khi đủ thông tin hoặc người dùng muốn kết thúc trò chuy ện(họ thường nói gián tiếp như tạm biệt, hoặc trực tiếp như yêu cầu kết thúc trò chuy ện), hãy tóm tắt thông tin và sử dụng nó làm đầu vào cho công cụ DSM5 .
Sau đó, hãy đưa ra tổng đoán về tình trạng sức khỏe tâm thần của người dùng.
Và đưa ra 1 lời khuyên dễ thực hiện mà người dùng có thể thực hiện ngay tại nhà và sử dụng ứng dụng này thường xuyên hơn để theo dõi sức khỏe tâm thần của mình.
Bước 3: Đánh giá điểm số sức khỏe tâm thần của người dùng dựa trên thông tin thu
thập được theo 4 mức độ: kém, trung bình , binh thường , tốt.
Sau đó lưu điểm số và thông tin vào file ."""

DEFAULT_SUMMARY_EXTRACT_TEMPLATE = """ \
Here is the content of the section :
{context_str}
Summarize the key topics and entities of the section . \
Summary : """

DEFAULT_KEYWORD_EXTRACT_TEMPLATE = """ \
{context_str}. Give {keywords} unique keywords for this \
document . Format as comma separated . Keywords : """

DEFAULT_QUESTION_ANSWERED_EXTRACTOR_TEMPLATE = """\
Here is the context :
{context_str}

Given the contextual information , \
generate {num_questions} questions this context can provide \
specific answers to which are unlikely to be found elsewhere .

Higher - level summaries of surrounding context may be provided \
as well . Try using these summaries to generate better questions \
that this context can answer ."""
