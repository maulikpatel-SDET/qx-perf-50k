"""Service module 49992: business logic, no crypto."""


def calculate_total_49992(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49992():
    return 'module 49992 handles orders and invoices'
