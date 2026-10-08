"""Service module 31327: business logic, no crypto."""


def calculate_total_31327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31327():
    return 'module 31327 handles orders and invoices'
