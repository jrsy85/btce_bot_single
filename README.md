btce_bot_single
===============

An automatic trading bot for btc-e.com.



  				LEGAL STATEMENT

		
		THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
		IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
		FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
		AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
		LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
		OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
		THE SOFTWARE.


This bot will buy on an uptrending market and sell on a downtrending market, it will only make one trade before
switching modes (buy/sell) and will allow for your threshold value between trades to compensate for the 0.2% transaction fee.


SELL LOGIC: If short average is lower than long average and the last price is higher than the last buy+threshold

BUY LOGIC: If short average is higher than long average and the last price is lower than the last sell-threshold
