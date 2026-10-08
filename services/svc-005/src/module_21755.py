"""Service module 21755: business logic, no crypto."""


def calculate_total_21755(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21755():
    return 'module 21755 handles orders and invoices'
