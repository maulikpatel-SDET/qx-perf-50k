"""Service module 49326: business logic, no crypto."""


def calculate_total_49326(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49326():
    return 'module 49326 handles orders and invoices'
