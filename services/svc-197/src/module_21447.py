"""Service module 21447: business logic, no crypto."""


def calculate_total_21447(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21447():
    return 'module 21447 handles orders and invoices'
