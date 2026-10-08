"""Service module 43157: business logic, no crypto."""


def calculate_total_43157(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43157():
    return 'module 43157 handles orders and invoices'
