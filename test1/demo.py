
class demo():
    def test1(self):
        ak = ApiKey()
        url = 'http://39.98.138.157:5000/api/login'
        data ={
            'username' : 'admin',
            'password' :'123456'
        }
        res = ak.do_post(url=url,json=data)
        self.assertEqua(res.status_code,200,msg='请求错误')
if __name__ == '__main__':
    pytest.main(['-s','demo,py'])