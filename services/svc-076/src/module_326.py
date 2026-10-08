"""Service module 326: business logic, no crypto."""


def calculate_total_326(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_326():
    return 'module 326 handles orders and invoices'
