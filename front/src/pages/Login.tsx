import React, {useState} from "react";
import * as Yup          from "yup";
import {useFormik}       from "formik";
import {useDispatch}     from "react-redux";
import authSlice         from "../store/slices/auth";
import axios             from "axios";
import {useHistory}      from "react-router";

// TODO: don't use explicit any if possible
// noinspection JSUnusedLocalSymbols
const Login = (props: any) => {
    const [message, setMessage] = useState ("");
    const [loading, setLoading] = useState (false);
    const dispatch = useDispatch ();
    const history = useHistory ();

    const handleLogin = (email: string, password: string) => {
        axios
            .post (`${process.env.REACT_APP_API_URL}/auth/login/`, {email, password})
            .then ((res) => {
                // noinspection JSVoidFunctionReturnValueUsed
                dispatch (
                    // TODO: POTENTIAL PROBLEM HERE, FUNCTION HAS INCORRECT ARITY THAN AXIOS EXPECTS??
                    // TODO: POTENTIAL PROBLEM HERE, FUNCTION RETURNS VOID BUT USING RETURN VALUE??
                    authSlice.actions.setAuthTokens ({
                        // @ts-ignore
                        token: res.data.access,
                        // @ts-ignore
                        refreshToken: res.data.refresh,
                    })
                );
                // TODO: POTENTIAL PROBLEM HERE, MAY NEED TO MODIFY CALL SIGNATURES
                // @ts-ignore
                // noinspection JSVoidFunctionReturnValueUsed @ts-ignore
                dispatch (authSlice.actions.setAccount (res.data.user));
                setLoading (false);
                history.push ("/", {
                    // @ts-ignore
                    userId: res.data.id
                });
            })
            .catch ((err) => {
                setMessage (err.response.data.detail.toString ());
            });
    };

    const formik = useFormik ({
        initialValues:    {
            email:    "",
            password: "",
        },
        onSubmit:         (values) => {
            setLoading (true);
            handleLogin (values.email, values.password);
        },
        validationSchema: Yup.object ({
            email:    Yup.string ().trim ().required ("What's your name?"),
            password: Yup.string ().trim ().required ("Please enter your password."),
        }),
    });

    return (
        <div className="Login">
            <h1>Login Here:</h1>
            <form onSubmit={formik.handleSubmit}>
                <input
                    id="email"
                    type="email"
                    placeholder="Email"
                    name="email"
                    value={formik.values.email}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.errors.email ? <div>{formik.errors.email} </div> : null}
                <input
                    id="password"
                    type="password"
                    placeholder="Password"
                    name="password"
                    value={formik.values.password}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                />
                {formik.errors.password ? (
                    <div>{formik.errors.password} </div>
                ) : null}
                <div hidden={false}>{message}</div>
                <button
                    type="submit"
                    disabled={loading}
                    className="rounded border-gray-300 p-2 w-32 bg-blue-700 text-white"
                >
                    Login
                </button>
            </form>
        </div>
    );
};

export default Login;
