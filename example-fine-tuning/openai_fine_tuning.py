import os
import openai

class OpenAITuning:
    def __init__(self):
        self.api_key = os.environ.get('APP_OPENAI_API_KEY')
        openai.api_key = self.api_key

    def upload_file(self, filename):
        with open(filename, "rb") as file:
            response = openai.File.create(
                file=file,
                purpose='fine-tune'
            )
        file_id = response['id']
        print(f"File uploaded successfully with ID: {file_id}")
        return file_id

    def fine_tune(self, file_id, model_name="gpt-3.5-turbo"):
        response = openai.FineTuningJob.create(
            training_file=file_id,
            model=model_name
        )
        job_id = response['id']
        print(f"Fine-tuning job created successfully with ID: {job_id}")
        return job_id

def main():
    tuning = OpenAITuning()
    file_id = tuning.upload_file("fsdl_berkeley_course_sample.jsonl")
    tuning.fine_tune(file_id)

if __name__ == "__main__":
    main()
