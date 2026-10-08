"""Service module 17324: business logic, no crypto."""


def calculate_total_17324(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17324():
    return 'module 17324 handles orders and invoices'
