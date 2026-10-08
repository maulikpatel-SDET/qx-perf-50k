"""Service module 27612: business logic, no crypto."""


def calculate_total_27612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27612():
    return 'module 27612 handles orders and invoices'
