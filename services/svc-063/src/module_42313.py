"""Service module 42313: business logic, no crypto."""


def calculate_total_42313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42313():
    return 'module 42313 handles orders and invoices'
