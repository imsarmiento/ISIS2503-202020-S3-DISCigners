import { FetchOptions } from './global';
export declare const createAbortController: () => AbortController;
export declare const fetchWithTimeout: (url: string, audience: string, scope: string, options: FetchOptions, worker?: Worker, timeout?: number) => Promise<any>;
export declare function getJSON<T>(url: string, timeout: number, audience: string, scope: string, options: FetchOptions, worker?: Worker): Promise<T>;
