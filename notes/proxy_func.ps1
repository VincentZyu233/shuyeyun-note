function ap {
    # 启用代理
    $Env:HTTP_PROXY = "http://127.0.0.1:7890"
    $Env:HTTPS_PROXY = "http://127.0.0.1:7890"

    Write-Host "代理已启用。正在测试连接..." -ForegroundColor Green
    
    try {
        # 使用 -Method Head 获取响应头
        $response = Invoke-WebRequest -Uri "https://www.google.com" -UseBasicParsing -Method Head -ErrorAction Stop

        # 打印状态码和部分内容
        Write-Host "代理测试成功！" -ForegroundColor Green
        Write-Host "--- 响应信息 ---"
        $response.Headers | Format-List
        Write-Host "----------------"
    }
    catch {
        Write-Host "代理测试失败！请检查代理服务是否运行。" -ForegroundColor Yellow
        Write-Host "详细错误: $($_.Exception.Message)"
    }
}

function dp {
    # 禁用代理
    $Env:HTTP_PROXY = $null
    $Env:HTTPS_PROXY = $null

    Write-Host "代理已禁用。" -ForegroundColor Red
}