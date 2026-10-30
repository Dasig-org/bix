declare const validators: Record<string, ((d: unknown) => boolean) & { errors?: { instancePath?: string; message?: string }[] | null }>;
export = validators;
