process run_python {
    output:
    path "status.log"

    script:
    """
    pip install requests
    python3 ${projectDir}/bin/prepare_fastqs.py
    """
}
