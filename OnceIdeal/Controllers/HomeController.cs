using OnceIdeal.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.IO;

namespace OnceIdeal.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }

        public ActionResult OnceIdeal()
        {
            return View(obtenerLista(serializar(@"C:\Users\qr362ep\Downloads\Sifut 11 Ideal\Sifut 11 Ideal\once.txt")));
        }

        public static List<List<Jugador>> obtenerLista(List<Jugador> lista)
        {
            List<List<Jugador>> once = new List<List<Jugador>>();

            for(int i = 0; i<4; i++)
            {
                once.Add(new List<Jugador>());
            }

            foreach (Jugador j in lista)
            {
                once[j.posicion - 1].Add(j);
            }

            return once;
        }

        public static List <Jugador> serializar(String archivo)
        {
            List<Jugador> lista = new List<Jugador>();
            String[] lineas = System.IO.File.ReadAllLines(archivo);

            foreach(String s in lineas)
            {
                lista.Add(convertirAJugador(s));
            }

            return lista;
        }

        public static Jugador convertirAJugador(String descripcion)
        {
            Jugador jugador = new Jugador();
            int guiones = 0;
            String s = "";

            foreach(char c in descripcion)
            {
                if (c.Equals('-'))
                {
                    switch (guiones)
                    {
                        case 0:
                            jugador.posicion = Convert.ToInt32(s);
                            s = "";
                            break;

                        case 1:
                            jugador.nombre = s;
                            s = "";
                            break;

                        case 2:
                            jugador.club = s;
                            s = "";
                            break;

                        case 3:
                            jugador.puntuacion = Convert.ToInt32(s);
                            break;

                        default:
                            break;
                    }
                    guiones++;

                }
                else
                {
                    s += c;
                }
            }

            return jugador;
        }
    }
}