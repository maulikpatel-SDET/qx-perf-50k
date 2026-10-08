"""Service module 26326: business logic, no crypto."""


def calculate_total_26326(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26326():
    return 'module 26326 handles orders and invoices'
