# ai-sqlrunner
ai-sqlrunnerは、OpenAIのGPT-4を用いて自然言語でのSQLコマンド実行を可能にするStreamlitアプリケーションです。<br />
本アプリケーションは、実行用途して作成したものです。<br />
実際SQL（DDL、DML、DCL）の実行されます。またその結果がGPTに送信される処理されるので<br />
機密情報が含むDBでの利用は控えることをおすすめします。

# Usage
1. git clone
    ```
    git clone git@github.com:opplol/ai-sqlrunner.git
    ```
2. input your api key in docker-compose.yml
    ```
        environment:
          - OPENAI_API_KEY={your openai api key}
    ```
3. docker compose up
    ```
    docker-compose up -d --build
    ```
4. access
    ```
    http://localhost:8501
    ```

# Development
use Vscode Remote Container
