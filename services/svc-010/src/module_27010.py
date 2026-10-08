"""Service module 27010: business logic, no crypto."""


def calculate_total_27010(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27010():
    return 'module 27010 handles orders and invoices'
