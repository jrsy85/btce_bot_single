
#
#  				LEGAL STATEMENT
#
#		
#		THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#		IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#		FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#		AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#		LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#		OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#		THE SOFTWARE.
#
#
#This bot will buy on an uptrending market and sell on a downtrending market, it will only make one trade before
#switching modes (buy/sell) and will allow for your threshold value between trades to compensate for the 0.2% transaction fee.


#SELL LOGIC: If short average is lower than long average and the last price is higher than the last buy+threshold
#BUY LOGIC: If short average is higher than long average and the last price is lower than the last sell-threshold


#Configuration
pair		= "ltc_btc"			#Pair to trade (ltc_btc, nmc_btc etc.)
tradex		= .5 				#Number of coins to buy (ltc, nmc etc.)
threshold 	= 0.3				#Percent threshold minimal (each trade costs 0.2%, 0.3% is recommended)
wait 		= 60				#Seconds wait between checks (15 seconds recommended minimum)
reset		= 720				#number of cycles since last sale to reset prices (in case market moves out oF bounds of the bot)
av_short	= 2				#short time average length (no. of cycles)
av_long		= 5				#long time average length (no. of cycles)
api_key 	= "INSERT-KEY-HERE"
api_secret 	= "INSERT-SECRET-HERE"


# If you find this script useful, donations are most welcome :)
# BTC: 18jQCcWprvqwmkKXLnGHnBtya4P8hoACL9
# LTC: LWv2cevauZsmD2vAgkhpBHTqmiC2CqwgY8
