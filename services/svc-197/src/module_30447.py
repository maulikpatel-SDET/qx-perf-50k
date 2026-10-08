"""Service module 30447: business logic, no crypto."""


def calculate_total_30447(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30447():
    return 'module 30447 handles orders and invoices'
