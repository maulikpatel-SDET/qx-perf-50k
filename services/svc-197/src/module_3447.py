"""Service module 3447: business logic, no crypto."""


def calculate_total_3447(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3447():
    return 'module 3447 handles orders and invoices'
