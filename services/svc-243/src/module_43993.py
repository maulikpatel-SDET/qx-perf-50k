"""Service module 43993: business logic, no crypto."""


def calculate_total_43993(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43993():
    return 'module 43993 handles orders and invoices'
